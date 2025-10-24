# Productivity Prediction of Garment Employees

## Information:

**Repository:** UCI Machine Learning.

[Dataset Link](https://archive.ics.uci.edu/dataset/597/productivity+prediction+of+garment+employees)

**Description:** This dataset includes important attributes of the garment manufacturing process and the productivity of employees, which were collected manually and validated by industry experts.

**Associated Tasks:** Regression and Classification.

**Number of Attributes:** 15.

**Task to Perform:** Regression.

**Number of Observations:** 1197.

**Target Variable:** `actual_productivity`

**Objective:** Predict the potential performance of employees under certain working conditions in order to control them and achieve a significant improvement in the company's productivity.

**Attribute information:**

| Variable              | Type        | Description                                                                                                 |
|-----------------------|-------------|-------------------------------------------------------------------------------------------------------------|
| Date                  | Categorical | Date in MM-DD-YYYY format when the data was recorded.                                                       |
| Quarter               | Categorical | A portion of the month. A month can be divided into four parts.                                             |
| Department            | Categorical | Department associated with the instance.                                                                    |
| Day                   | Categorical | Day of the week.                                                                                            |
| Team                  | Numeric     | Team number associated with the instance.                                                                   |
| Targeted_productivity | Numeric     | Productivity target set by the Authority for each team for each day.                                        |
| Smv                   | Numeric     | Standard Minute Value, the time it would take a qualified staff member to perform the task.                 |
| Wip                   | Numeric     | Work in progress. Includes the number of unfinished items for products.                                     |
| Over_time             | Numeric     | Represents the amount of overtime for each team in minutes.                                                 |
| Incentive             | Numeric     | Represents the amount of the financial incentive (in BDT) that allows or motivates a certain course of action.|
| Idle_time             | Numeric     | The time during which production was interrupted for various reasons.                                       |
| Idle_men              | Numeric     | Number of idle workers due to production interruption.                                                      |
| No_of_style_change    | Numeric     | Number of changes in the style of a certain product.                                                        |
| No_of_workers         | Numeric     | Number of workers in each team.                                                                             |
| `actual_productivity` | Numeric     | The actual percentage of productivity contributed by the workers. Ranges from 0 to 1.                       |

## Business Understanding:

In the garment industry, as in any other process where humans are primarily responsible for execution, a multitude of factors can influence overall performance due to the individual performance of each person involved. Therefore, it is crucial to understand which variables can (or cannot) be controlled and how they affect employee performance. This understanding allows for the development of strategies to prevent productivity from declining. With this in mind, the following analyses are proposed:

- **Actual Productivity vs. Day of the Week:** It may seem minor, but under otherwise equal conditions, the day of the week can influence employee productivity. For example, motivation might be lower on a Friday as the weekend approaches. A graph showing the average actual productivity for each day of the week will be created to investigate this.

- **Actual Productivity vs. Targeted Productivity:** Setting a goal is a significant stimulus that can determine the effort a person puts into a task. However, this can vary from person to person; some may be motivated to exceed expectations, while others may become discouraged if they perceive the goal as too difficult. Therefore, it is important to observe how the targeted productivity (goal) influences actual productivity.

- **Actual Productivity vs. Date:** Similar to the days of the week, there may be certain times of the year when productivity increases or decreases. This could be due to demand for certain holidays or even the season. A graph will be created to observe the months of the year with the highest productivity.

- **Actual Productivity vs. Department:** It is common for a company to have different phases to complete a task. Each phase may have a different level of complexity and may require specialized personnel. In this case, there are two departments: one for sewing and one for finishing. It would be interesting to create a graph that compares the actual productivity of each department and to study why one department might have better productivity than the other.

If the focus were not on actual productivity, other graphs could be considered to observe different behaviors among the variables, such as **Number of Workers vs. SMV**. This would allow us to see the relationship between the complexity of the tasks (more or less time taken by a qualified staff member) and the number of workers assigned. However, for the purposes of this project and the desired task, these other possible graphs were not created.
