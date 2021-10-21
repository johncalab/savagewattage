import streamlit as st
from savagewattage.intervals import Interval
from savagewattage.templates import templates
from savagewattage.ramp import estimate_ftp

with st.sidebar:
    st.markdown("# SavageWattage")
    selection = st.radio("",["Zones","Ramps"])

if selection == "Zones":
    st.markdown("### Zones Calculator")
    ftp = st.number_input(
        label = "Enter FTP:",
        min_value = 0,
        max_value = 999,
        step = 1,
    )

    for templ in templates:
        st.text(str(Interval.from_template(ftp=ftp,template=templ)))

if selection == "Ramps":
    st.markdown("### Ramp Test Calculator")
    st.markdown(
        """
        Protocol:
        * Warm up.
        * Start at 100W.
        * Every 150seconds increase by 25W.
        * Go until failure.

        Record two things:
        * wattage of last SUCCESSFUL ramp
        * seconds (if any) of last failed ramp
        """
    )

    with st.expander("Show example"):
        st.markdown(
            """
            Example:
            - 150 seconds @100W
            - 150 seconds @125W
            - 150 seconds @150W
            - 150 seconds @175W
            - 150 seconds @200W
            - 150 seconds @225W
            - 150 seconds @250W
            - 150 seconds @275W
            - 150 seconds @300W
            - 13 seconds @325

            completed  = 300W, extra = 13s

            leading to an estimated ftp of: 249
            """
        )

    completed = st.number_input(
        label = "Enter the wattage of the last completed ramp:",
        min_value = 0,
        max_value = 975,
        step = 25,
    )
    if completed > 0:
        extra = st.number_input(
            label = "Enter the number of seconds of the last failed ramp:",
            min_value = 0,
            max_value = 150,
            step = 1,
        )
        est_ftp = estimate_ftp(completed=completed,extra=extra)

        st.text(f"Estimated ftp is {est_ftp}.")
