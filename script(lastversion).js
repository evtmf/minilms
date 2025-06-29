const lessons = [
  { id: "lesson1", title: "Мессенджер" },
  { id: "lesson2", title: "Почта" }
];

const list = document.getElementById("lesson-list");

lessons.forEach(lesson => {
  const li = document.createElement("li");
  const a = document.createElement("a");
  a.href = `scorm.html?lesson=${lesson.id}`;
  a.textContent = lesson.title;
  a.className = "lesson-link";
  li.appendChild(a);
  list.appendChild(li);
});
