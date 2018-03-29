        var canvas;
        var canvasContext;
        var gridWidth = 10;
        var gridHeight = 10;
        var boxHeight = 59;
        var boxWidth = 59;
        
        var grid = [];
            var row = [];
            for (i = 1; i < 11; i++) {
                row.push(i);
            }

            for (i = 1; i < 11; i++) {
                grid.push(row)
            }


        
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
            var data = canvasContext.getImageData(0, 0, 1, 1).data;
            
            var framesPerSecond=1;
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


        function drawEverything() {
            // draws the black background of the screen
            drawRect(0,0,canvas.width,canvas.height,'black');

            // draws the vertical lines
            for (i = 0; i < gridWidth + 1; i++) { 
                drawRect((canvas.width - 1)/gridWidth * i,0,1,canvas.height,'grey')
            }

            // draws the horizontal lines
            for (i = 0; i < gridHeight + 1; i++) {
                drawRect(0,(canvas.height - 1)/gridWidth * i,canvas.width,1,'grey')
            }

            drawRect(1,1,boxWidth,boxHeight,'red');
            drawRect(61,1,boxWidth,boxHeight,'red');
            console.log(grid);

            checkColor(4,4);
            checkColor(10,4);
            checkColor(16,4);
            

            
            document.getElementById("test").innerHTML = "There!";

        }

        function drawRect(leftX,topY,width,height,drawColor) {
            canvasContext.fillStyle = drawColor;
            canvasContext.fillRect(leftX,topY,width,height);
        }

        function checkColor(xPosition, yPosition) {
            data = canvasContext.getImageData(xPosition, yPosition, 1, 1).data;
            
        }