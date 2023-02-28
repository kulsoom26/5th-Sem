var title1Text="Ca.bro.kies"
		var t1=document.getElementById('title1')
		var t2=document.getElementById('title2')
		var i=0
		console.log(t1)

		function typeTitle(){
			console.log(title1Text.charAt(i))
			if(i<title1Text.length){
				t1.innerText+=title1Text.charAt(i)
				setTimeout(typeTitle,150)
			}
			if(i==title1Text.length){
				t2.innerText+="Cakes "
				setTimeout(typeTitle,250)
			}
			if(i==title1Text.length+1){
				t2.innerText+=" Brownies "
				setTimeout(typeTitle,250)
			}
			if(i==title1Text.length+2){
				t2.innerText+=" Cookies "
				setTimeout(typeTitle,250)
			}
			i++
		}

        var layer1=document.getElementById('layer1')
        var layer2=document.getElementById('layer2')
        var layer3=document.getElementById('layer3')
        var icing1=document.getElementById('icing1')
        var icing2=document.getElementById('icing2')   
		var candle=document.getElementById('candle')
		var flame=document.getElementById('flame')
        var cake=false
        var posL1=100
		var posL2=100
		var posL3=100
        var posI1=100
		var posI2=100
		var posC=100
		var color=0
        var timer=null

		function makeCake(){
            layer1.style.display="block"
            layer1.style.top=posL1+'px'
            clearInterval(timer)
            timer=setInterval(frame,1)
            function frame(){
                if(posL1 < 350){
                    posL1++
                    layer1.style.top=posL1+'px'
                    console.log(layer1.style.top)
                }
                else if(posI1 == 100){
                    icing1.style.display="block"
                    icing1.style.top=posI1+'px'

                    posI1++
                }
                else if (posI1 < 340){
                    posI1++
                    icing1.style.top=posI1+'px'
                    console.log(icing1.style.top)
                }
				else if(posL2 == 100){
                    layer2.style.display="block"
                    layer2.style.top=posL2+'px'

                    posL2++
                }
				else if(posL2 < 290){
                    posL2++
                    layer2.style.top=posL2+'px'
                    console.log(layer2.style.top)
                }
				else if(posI2 == 100){
                    icing2.style.display="block"
                    icing2.style.top=posI2+'px'

                    posI2++
                }
                else if (posI2 < 280){
                    posI2++
                    icing2.style.top=posI2+'px'
                    console.log(icing2.style.top)
                }
				else if(posL3 == 100){
                    layer3.style.display="block"
                    layer3.style.top=posL3+'px'

                    posL3++
                }
				else if(posL3 < 230){
                    posL3++
                    layer3.style.top=posL3+'px'
                    console.log(layer3.style.top)
                }
				else if(posC == 100){
					candle.style.display="block"
					candle.style.top=posC+"px"
					posC++
				}
				else if(posC < 180){
					posC++
					candle.style.top=posC+'px'
					console.log("candle")
					console.log(candle.style.top)
				}
                else{
					clearInterval(timer)
					flameAppear()
                    flameCall()
                }
            }
		}

		function flameCall(){
			timer = setInterval(flameAppear,500)
		}

        function flameAppear(){
			if (color == 0){
				flame.style.display="block"
				flame.style.backgroundColor="#e26023"
				flame.style.height="20px"
				color ++
			}
			else if (color == 1){
				flame.style.display="none"
				color++
			}
			else if (color == 2){
				flame.style.display="block"
				flame.style.backgroundColor="#f07f4b"
				flame.style.height="15px"
				color ++
			}
			else {
				flame.style.display="none"
				color= color - 3
			}
        }