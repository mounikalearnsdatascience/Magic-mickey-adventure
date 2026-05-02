let points = 0;

function callMickey() {
  document.getElementById("door").innerHTML = "🐭";
  document.getElementById("message").innerHTML = "Mickey came out! Hi friend!";
}

function giveCheese() {
  points += 10;
  document.getElementById("message").innerHTML = "Mickey loved the cheese! +10 points";
  document.getElementById("points").innerHTML = "Friendship Points: " + points;
}

function goAdventure() {
  points += 20;
  document.getElementById("message").innerHTML = "You both went on a magical adventure! +20 points";
  document.getElementById("points").innerHTML = "Friendship Points: " + points;
}
