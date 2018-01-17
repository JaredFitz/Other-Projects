        var canvas;
        var canvasContext;
        var ballX = 50;
        var ballSpeedX = 5;
        var ballY = 50;
        var ballSpeedY = Math.floor(Math.random()*5);
        var ballRadius = 15;
        var paddleWidth = 10;
        const paddleHeight = 100;
        var paddle1Y = 250;
        var paddle2Y = 250;
        var difficulty = 6;
        
        var player1Score = 0;
        var player2Score = 0;
        const winningScore = 3;

        var showingWinScreen = false;

        function calculateMousePosition(evt) {
            var rect = canvas.getBoundingClientRect();
            var root = document.documentElement;
            var mouseX = evt.clientX - rect.left;
            var mouseY = evt.clientY - rect.top;
            return {
                x:mouseX,
                y:mouseY
            };
        }

        function handleMouseClick(evt) {
            if (showingWinScreen) {
                player1Score = 0;
                player2Score = 0;
                showingWinScreen = false;
            }
        }

        window.onload = function() {
            canvas = document.getElementById('gameCanvas');
            canvasContext = canvas.getContext('2d');
            canvasContext.font = "30px Arial";

            var framesPerSecond=60;
            setInterval(function() {
                moveEverything();
                drawEverything();
            },1000/framesPerSecond);

            canvas.addEventListener('mousedown',handleMouseClick);

            canvas.addEventListener('mousemove',
            function(evt) {
                var mousePosition = calculateMousePosition(evt);
                paddle1Y = mousePosition.y - (paddleHeight / 2);
            });
        }

        function ballReset() {
            if (player1Score >= winningScore || player2Score >= winningScore) {
                showingWinScreen = true;
            }
            ballX = canvas.width / 2;
            ballY = canvas.height / 2;
            ballSpeedY = Math.floor(Math.random()*5);
            ballSpeedX *= -1;
        }

        function computerMovement(){
            if (paddle2Y + paddleHeight/2 < ballY - 35) {
                paddle2Y += difficulty;
            } else if (paddle2Y + paddleHeight/2 > ballY + 35) {
                paddle2Y -= difficulty;
            }
        }

        function moveEverything() {
            if (showingWinScreen) {
                return;
            }
            computerMovement();
            // left wall and paddle
            if (ballX - ballRadius <= paddleWidth) {
                if (ballY >= paddle1Y && ballY < paddle1Y + paddleHeight) {
                    ballSpeedX = -ballSpeedX;
                    var deltaY = ballY - (paddle1Y + paddleHeight/2);
                    ballSpeedY = deltaY * .2;
                } else {
                    player2Score++;
                    ballReset();
                }
            }
            
            // right wall and paddle
            if (ballX + ballRadius >= canvas.width - paddleWidth) {
                if (ballY >= paddle2Y && ballY < paddle2Y + paddleHeight) {
                    ballSpeedX = -ballSpeedX;
                    var deltaY = ballY - (paddle2Y + paddleHeight/2);
                    ballSpeedY = deltaY * .2;
                } else {
                    player1Score++;
                    ballReset();
                }
            }

            if (ballY + ballRadius >= canvas.height) {
                ballSpeedY = -ballSpeedY;
            }

            if (ballY - ballRadius <= 0) {
                ballSpeedY = -ballSpeedY;
            }
            
            ballX += ballSpeedX;
            ballY += ballSpeedY;
        }

        function drawNet() {
            for (var i=0;i<canvas.height;i+=40) {
                drawRect(canvas.width/2 - 2,i,4,20,'white');
            }
        }

        function drawEverything() {
            // draws the black background of the screen
            drawRect(0,0,canvas.width,canvas.height,'black');

            if (showingWinScreen) {
                canvasContext.fillStyle = 'white'
                if (player1Score >= winningScore) {
                    canvasContext.fillText("You win! Click to continue",180,100);
                } else {
                canvasContext.fillText("Computer wins! Click to continue",180,100);
                }
                return;
            }
            drawNet();
            // draws the left player paddle
            drawRect(0,paddle1Y,paddleWidth,paddleHeight,'white');

            // draws the right computer paddle
            drawRect(canvas.width-paddleWidth,paddle2Y,paddleWidth,paddleHeight,'white');

            // draws the ball
            drawCircle(ballX, ballY, ballRadius, 'white');

            canvasContext.fillText(player1Score, 100, 100);
            canvasContext.fillText(player2Score,700,100);
        }

        function drawRect(leftX,topY,width,height,drawColor) {
            canvasContext.fillStyle = drawColor;
            canvasContext.fillRect(leftX,topY,width,height);
        }

        function drawCircle(centerX, centerY, radius, drawColor) {
            canvasContext.fillStyle = drawColor;
            canvasContext.beginPath();
            canvasContext.arc(centerX, centerY, radius, 0, Math.PI*2, true);
            canvasContext.fill();
        }