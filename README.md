# Home Automation Server

## Installation

*Prerequisites: You must have python and pip (python package manager) installed.*

From the project's root directory:

1. Install virtualenv for creating a self contained python environment.
	`sudo pip install virtualenv`

2. Create a new python virtual environment.
	`virtualenv venv`

3. Start the new virtual environment.
	`source venv/bin/activate`

4. Install project's dependencies.
	`pip install -r requirments.txt`

## Usage

1. Start the home automation server.
	`python HomeAutomationServer.py`

2. Visit the home automation server by navigation to http://localhost:5000 in your browser.

## Development

In order to add new functionality to your home automation server, you must do the following:

1. Add a new python "endpoint" function that performs the task in HomeAutomationServer.py.

  ```
  @app.route('/my_cool_automation_task')
  def my_cool_automation_task():
      """Performs my cool home automation task"""
      #INSERT CODE HERE
      return jsonify(result="Cool task performed succesfully!")
  ```

2. Add a button to your webpage that corresponds to the new task in templates/index.html.

  ```
  <button id="do_my_cool_automation_task">Do My Cool Automation Task</button>
  ```

3. Write a Javascript function that calls your corresponding python "endpoint" and prints out
the result to the html in index.html.

  ```
  var doMyCoolAutomationTask = function(e) {
    $.get($SCRIPT_ROOT + '/my_cool_automation_task', function(data) {
      $('#result').text(data.result);
    });
  };
  ```

4. Attach a "listener" to your button's "click" event that calls your new Javascript function.

  ```
  $('button#do_my_cool_automation_task').bind('click', doMyCoolAutomationTask);
  ```

5. Restart automation server and celebrate!