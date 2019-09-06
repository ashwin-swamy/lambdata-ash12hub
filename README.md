# lambdata_ash12hub

## Usage
```python
import lambdata_ash12hub;
```
The `lambdata_ash12hub` directory contains some basic Data Science methods.

## Methods
The Methods included in the directory are:
```python
lambdata_ash12hub.train_validation_test_split(x, y, train_size=0.8, val_size=0.1, test_size=0.1, random_state=None, shuffle=True)
```
Takes a dataset used to predict the model and splits it into training, validation and testing data.

The method takes in the following parameters:
- Required

  | Parameter | Description |
  | :- | :- |
  | `x` | The data which includes the features used for the model. |
  | `y` | The data which includes the field that is being predicted. |
- Optional

  | Parameter | Description |
  | :- | :- |
  | `train_size` | The size of the training dataset compared to the original dataset. Has a range of 0-1. |
  | `val_size` | The size of the validation dataset compared to the original dataset. Has a range of 0-1. |
  | `test_size` | The size of the testing dataset compared to the original dataset. Has a range of 0-1. |
  | `random_state` | The seed used by the random number generator. |
  | `shuffle` | Whether or not the data should be shuffled before splliting it. |


```python
return x_train, x_val, x_test, y_train, y_val, y_test;
```
The method returns:

| Variable | Description |
| :- | :- |
| `x_train` | The training data of the x dataset. |
| `x_val` | The validation data of the x dataset. |
| `x_test` | The testing datasets of the x dataset. |
| `y_train` | The training data of the y dataset. |
| `y_val` | The validation data of the y dataset. |
| `y_test` | The testing datasets of the y dataset. |


```python
lambdata_ash12hub.split_date_list(date_list)
```
Splits a list of dates into day, month and year.

The method takes in the following parameters:
- Required

  | Parameter | Description |
  | :- | :- |
  | `date_list` | The list of dates to split. |

```python
return day, month, year;
```
The method returns:

| Variable | Description |
| :- | :- |
| `day` | List of days from `date_list`. |
| `month` | List of months from `date_list`. |
| `year` | List of years from `date_list`. |

```python
lambdata_ash12hub.  add_new_column(new_list)
```


The method takes in the following parameters:
- Required

| Parameter | Description |
| :- | :- |
| `new_list` | The list to be made a Pandas Series. |

```python
return new_column;
```
The method returns:

| Variable | Description |
| :- | :- |
| `new_column` | The new column ready to be added to a dataset. |
