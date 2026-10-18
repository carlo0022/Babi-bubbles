# Week 17 Test Cases

**Project:** Simulated Device Monitoring and Alert System  


| Test ID | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Displays all five initial readings | Displays five readings | Pass |
| TC02 | Choose 2, enter 33 | Reading added successfully | Reading added successfully | Pass |
| TC03 | Choose 2, enter `abc` | Rejects non-numeric input | Input rejected | Pass |
| TC04 | Choose 2, enter -5 | Rejects negative reading | Input rejected | Pass |
| TC05 | Choose 2, enter 120 | Rejects value above 100 | Input rejected | Pass |
| TC06 | Classify 30 °C | WARNING | WARNING | Pass |
| TC07 | Classify 35 °C | WARNING | WARNING | Pass |
| TC08 | Choose 4 with initial readings | Total 160, average 32.00 °C, minimum 28 °C, maximum 37 °C, status ATTENTION REQUIRED | Summary matches expected values | Pass |
| TC09 | Enter menu choice 9 | Shows invalid-choice message and repeats menu | Invalid-choice message displayed | Pass |
| TC10 | Choose 5 | Displays exit message and ends program | Exit message displayed | Pass |

## Additional Input Validation

| Input | Expected Result |
|---|---|
| Empty input | Rejects empty reading |
| `3.5` | Rejects non-integer input |
| `0` | Accepts reading |
| `100` | Accepts reading |
| `101` | Rejects out-of-range reading |

## Bug Notes
Record any bugs found during