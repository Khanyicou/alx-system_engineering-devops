import requests
import sys

def get_employee_todo_progress(employee_id):
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + "users/{}".format(employee_id))
    user_data = user_response.json()
    
    if user_response.status_code != 200:
        print("Error: User not found.")
        return

    todos_response = requests.get(url + "todos", params={"userId": employee_id})
    todos_data = todos_response.json()
    
    if todos_response.status_code != 200:
        print("Error: TODO list not found for the user.")
        return

    completed_tasks = [task for task in todos_data if task["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)
    
    print("Employee {} is done with tasks({}/{}):".format(user_data["name"], num_completed_tasks, total_tasks))
    for task in completed_tasks:
        print("\t{}".format(task["title"]))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
        
    employee_id = sys.argv[1]
    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
        
    get_employee_todo_progress(employee_id)
