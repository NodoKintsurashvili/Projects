let tasks = []
let currentFilter = "all"
const API_URL = "http://127.0.0.1:8000/tasks"


async function fetchTasks(){
  const response = await  fetch(API_URL)
  const data = await response.json()
  tasks = data
  render()  
}

function createElement(type, className, text){
  let el = document.createElement(type)
  if (className) el.classList.add(className)
  if (text) el.textContent = text
  return el
}

async function addTask(){
  let input = document.getElementById("myInput")
  let value = input.value
  if(value.trim() === "") return

  await fetch(API_URL, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({title: value, completed: false})
  })
  input.value = ""
  fetchTasks()
}


function editTask(task, textElement){
  let input = createElement("input", "text")
  input.value = task.title

  textElement.replaceWith(input)

  input.focus()

  input.addEventListener("keyup", async (e) => {
    if(e.key === "Enter"){
        await fetch(`${API_URL}/${task.id}`, {
          method: "PUT",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({title: input.value, completed: task.completed})
        })
        fetchTasks();
    }
    if(e.key === "Escape"){
      render()
    }
  })
}

function createTaskElement(task){
  let taskBox = createElement("div", "task")

  let text = createElement("div", "text", task.title)
  if(task.completed){
    text.classList.add("done")
  }
  let checkBoxDiv = createElement("div", "checkBoxDiv")
  let checkBox = createElement("input", "checkBox")
  checkBox.type = "checkbox"
  checkBox.checked = task.completed

  let buttonDiv = createElement("div", "buttonDiv")
  let button = createElement("button", "delButton", "Delete")


  text.addEventListener("dblclick", async () => {
    editTask(task, text)
  })

  checkBox.addEventListener("change", async () => {
    text.classList.toggle("done", checkBox.checked)
    await fetch(`${API_URL}/${task.id}`, {
      method: "PUT",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({title: task.title, completed: checkBox.checked})
    })
  })

  button.addEventListener("click", async () => {
    await fetch(`${API_URL}/${task.id}`, {method: "DELETE"})
    fetchTasks()
  })

  checkBoxDiv.appendChild(checkBox)
  buttonDiv.appendChild(button)
  taskBox.appendChild(text)
  taskBox.appendChild(checkBoxDiv)
  taskBox.appendChild(buttonDiv)

  return taskBox
}

function render(){
  let app = document.getElementById("taskBox")
  app.innerHTML = ""

  let filtered = tasks

  if (currentFilter === "active"){
    
    filtered = tasks.filter(t => !t.completed)
  }

  if (currentFilter === "completed"){
    filtered = tasks.filter(t => t.completed)
  }

  filtered.forEach(task => {
    app.appendChild(createTaskElement(task))
  })
}

fetchTasks();

document.getElementById("add").addEventListener("click", addTask)

document.getElementById("myInput").addEventListener("keyup", (e) => {
  if (e.key === "Enter"){
    addTask()
  }
})

document.getElementById("myBox").addEventListener("change", (e) => {
  currentFilter = e.target.value
  render()
})