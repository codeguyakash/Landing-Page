let timer = setInterval(updateCounter, 50);

function updateCounter() {
  let counterElement = document.getElementById("counter1");
  let counterElement2 = document.getElementById("counter2");
  let counterElement3 = document.getElementById("counter3");
  let count = parseInt(counterElement.textContent);
  if (count == 399) {
    clearInterval(timer);
  }
  count++;
  counterElement.textContent = count;
  counterElement2.innerText = count;
  counterElement3.innerText = count;
}
