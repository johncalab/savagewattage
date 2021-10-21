import streamlit as st
from savagewattage.intervals import Interval
from savagewattage.templates import templates
from savagewattage.ramp import estimate_ftp

with st.sidebar:
    st.markdown("# SavageWattage")
    selection = st.radio("",["Zones","Ramps"])

if selection == "Zones":
    st.markdown("### Zones Calculator")
    ftp = int(st.number_input("Enter FTP:"))

    if ftp > 0:
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

    completed = int(st.number_input("Enter the wattage of the last completed ramp:"))
    if completed > 0:
        extra = int(st.number_input("Enter the number of seconds of the last failed ramp:"))
        est_ftp = estimate_ftp(completed=completed,extra=extra)

        st.text(f"Estimated ftp is {est_ftp}.")
