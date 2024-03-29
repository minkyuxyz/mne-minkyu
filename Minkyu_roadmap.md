# Roadmap Friday July 14th
_Last Updated: July 21st_

Purpose: First empirical evidence of the maintenance of our previous error
(memory of error) during motor learning and description of the spatiotemporal dynamics of the 
neural representation

Test at the individual level and at the group level (14 participants)

## Decoding the memory of error with GeneralizingEstimator in sensors space
### Pre-processing, ICA (_ongoing..._)
- [x] Create epochs and decode target, movement direction and error
- [ ] Cleaning data: remove blink component with ICA (or others)
- [ ] Cleaning data: remove heart beat component with ICA (or others)
- [ ] Test the robustness of decoding with and without cleaning the data
### Decoding
- [x] Decode with all existing variables, and plot them
    * _saved in_ mk_results/
- [ ] Test which measure of error is the most reliable in term of decoding
- [x] Epoch the data with the movement onset and not the target onset as a reference time
    * _saved in_ RAW_DATA/mvnt_onset
- [ ] Identify the duration of the memory of error (one, two, three trials...)
- [ ] Test the decoding of the error in stable vs. random environment
- [ ] Generalize over condition: apply target decoding to error decoding (to test if our error decoding is specific to the error and not related to the target)

## Time-frequency domain
- [ ] Decode in time-frequency with CSP (for classification) or sPoc (for regression)

## Topography and sources
- [x] Plot the patterns and filters of the decoding results
    * _saved in_ mk_results/plots
- [ ] Create the source pipeline and make source reconstruction
- [ ] Decode in source on a trial by trial basis

## Appointments!
- [ ] 10 AM, July 24th, with Ethan
- [ ] 1 PM, July 24th, with Sarah
