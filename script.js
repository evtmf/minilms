const tg = window.Telegram.WebApp;
tg.expand();  // делаем окно большим

document.getElementById("startLesson").addEventListener("click", () => {
  tg.MainButton.text = "Продолжить обучение";
  tg.MainButton.show();
});
