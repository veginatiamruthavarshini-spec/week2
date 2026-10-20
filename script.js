document.getElementById("studentForm").addEventListener("submit", function(e){
  e.preventDefault();
  let name = document.getElementById("name").value;
  let email = document.getElementById("email").value;
  let dept = document.getElementById("dept").value;

  let li = document.createElement("li");
  li.textContent = name + " - " + email + " - " + dept;
  document.getElementById("studentList").appendChild(li);

  this.reset();
});
