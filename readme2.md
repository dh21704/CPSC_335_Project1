# Algorithm 2 README

## Overview / Description

This algorithm receives:

* `schedules`: a list of busy intervals for each person (in `"HH:MM"` format).
* `daily_times`: a list of each person’s daily start and end times (in `"HH:MM"` format).
* `duration`: the minimum meeting length in minutes.

The algorithm finds common free time slots of at least `duration` minutes where all people are available.

---

## Installation / Setup

Need:

* Python installed on your computer (any version ≥3.x).
* An IDE or online editor to run Python code.

---

## Usage / Examples

Call the `group_schedule()` function and pass:

* A list of schedules (busy intervals) for each person.
* A list of daily start and end times for each person.
* A duration in minutes.

**Example:**

```python
person1_Schedule = [["7:00","8:30"],["12:00","13:00"],["16:00","18:00"]]
person1_DailyAct = ["9:00","19:00"]

person2_Schedule = [["9:00","10:30"],["12:20","14:00"],["14:30","15:00"],["16:00","17:00"]]
person2_DailyAct = ["9:00","18:30"]

schedules = [person1_Schedule, person2_Schedule]
daily_times = [person1_DailyAct, person2_DailyAct]

print(group_schedule(schedules, daily_times, 30))
```

**Output:**

```
[['10:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]
```
