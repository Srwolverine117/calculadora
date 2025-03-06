Preguntas 

Que hace document.querySelector(".display"); ? 
Que hace const buttons = document.querySelectorAll("button"); ? 
Que hace buttonText = button.textContent; ? 
Que hace y como funciona buttons.forEach((button) => { ...} ? 
Que hace y como funciona button.addEventListener("click", () => { } ) 

Respuestas

document.querySelector(".display"); 
• Selecciona el primer elemento con la clase .display. 
const buttons = document.querySelectorAll("button"); 
• Selecciona todos los elementos <button> y devuelve una NodeList. 
buttonText = button.textContent; 
• Obtiene el texto dentro del botón, incluyendo contenido oculto. 
buttons.forEach((button) => { ... } ) 
• Recorre cada botón en la NodeList y ejecuta la función dentro del bloque { ... }. 
button.addEventListener("click", () => { } ) 
• Escucha el evento "click" en el botón y ejecuta la función cuando se haga clic.
