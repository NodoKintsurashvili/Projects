let tasks = []
let currentFilter = "all"

function createElement(type, className, text){
  let el = document.createElement(type)
  if (className) el.classList.add(className)
  if (text) el.textContent = text
  return el
}

function changeState(checkBox, text){
  text.classList.toggle("done", checkBox.checked)
}

function addTask(){
  let input = document.getElementById("myInput")
  let value = input.value

  if (value.trim() === "") return

  tasks.push({
    id: Date.now(),
    text: value,
    completed: false
  })

  input.value = ""
  render()
}

function deleteTask(id){
  tasks = tasks.filter(t => t.id !== id)
  render()
}

function editTask(task, textElement){
  let input = createElement("input", "text")
  input.value = task.text

  textElement.replaceWith(input)

  input.focus()

  input.addEventListener("keyup", (e) => {
    if(e.key === "Enter"){
      task.text = input.value
      task.completed = false
      render()
    }
    if(e.key === "Escape"){
      render()
    }
  })
}

function createTaskElement(task){
  let taskBox = createElement("div", "task")

  let text = createElement("div", "text", task.text)
  let checkBoxDiv = createElement("div", "checkBoxDiv")
  let checkBox = createElement("input", "checkBox")
  checkBox.type = "checkbox"
  checkBox.checked = task.completed

  let buttonDiv = createElement("div", "buttonDiv")
  let button = createElement("button", "delButton", "Delete")


  text.addEventListener("dblclick", () => {
    editTask(task, text)
  })

  checkBox.addEventListener("change", () => {
    task.completed = checkBox.checked
    render()
  })

  button.addEventListener("click", () => {
    tasks = tasks.filter(t => t.id !== task.id)
    render()
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