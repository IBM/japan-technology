function drawStripe(context, startx, starty, endx, endy) {
  context.beginPath();
  context.strokeStyle = "white";
  context.lineWidth = 2;
  context.lineCap = 'round';
  context.moveTo(startx, starty);
  context.lineTo(endx, endy);
  context.stroke();
}

function fillStripes(context, x, y, width, height) {

  var starty = y;
  var endx = x;
  var startx = x;
  var endy = y;

  var gap = 5;

  do {
    starty = starty + gap;
    endx = endx + gap;
    drawStripe(context, startx, starty, endx, endy)
  } while (starty < height + y && endx + 5 < width + x)

  if (width > height) {

    endx = height + x;

    do {
      starty = height + y;
      startx = startx + gap;
      endx = endx + gap;
      drawStripe(context, startx, starty, endx, endy)
    } while (endx + gap < width + x)

    endx = x + width
    endy = y - gap;
    starty = y + height;

    do {
      startx = startx + gap;
      endy = endy + gap;
      drawStripe(context, startx, starty, endx, endy)
    } while (endy + gap < height + y)
  }

  if (height > width) {

    endx = width + x;
    endy = y - gap;
    startx = x;
    starty = width + y - gap;

    do {
      starty = starty + gap;
      endy = endy + gap;
      drawStripe(context, startx, starty, endx, endy)
    } while (starty + gap < height + y)

    starty = y + height - gap;
    startx = x;
    endx = x + width;

    do {
      startx = startx + gap;
      endy = endy + gap;
      drawStripe(context, startx, starty, endx, endy)
    } while (startx + gap < width + x)
  }
}
