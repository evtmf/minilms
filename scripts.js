const lessons = [
    { id: "lesson1", title: "Мессенджер" },
    { id: "lesson2", title: "Почта" }
  ];
  
  function init() {
    const list = document.getElementById('lesson-list');
    
    // Очищаем на случай ошибок
    list.innerHTML = '';
  
    // Заполняем список
    lessons.forEach(lesson => {
      const li = document.createElement('li');
      const link = document.createElement('a');
      
      link.href = `scorm.html?lesson=${lesson.id}`;
      link.textContent = lesson.title;
      link.className = 'lesson-link';
      
      li.appendChild(link);
      list.appendChild(li);
    });
  }
  
  // Запускаем после загрузки страницы
  document.addEventListener('DOMContentLoaded', init);