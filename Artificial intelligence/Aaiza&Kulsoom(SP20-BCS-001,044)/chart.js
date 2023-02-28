var valid = [true,true,true,true,true]

		function checkInput(type){
			var namePattern = /^[^1-9]*$/
			var phonePattern = /^[0-9]{11}$/
			var emailPattern = /^([a-z0-9\.-]+)@([a-z0-9-]+)\.([a-z]{2,8})$/
			var input = document.getElementById(type)
			var text = document.getElementById(type+'Error')
			var form = document.getElementById(type+'Form')
			var value = input.value

			console.log(valid)
			if(type == 'name'){
				if(value=="" || !(namePattern.test(value))){
					text.innerHTML="name should only contain letters"
					input.classList.remove("is-valid")
					input.classList.add("is-invalid")
					valid[0]=false
				}
				else{
					text.innerHTML=""
					input.classList.remove("is-invalid")
					input.classList.add("is-valid")
					valid[0]=true
				}
			}
			if(type == 'email'){
				if(emailPattern.test(value)){
					text.innerHTML=""
					input.classList.remove("is-invalid")
					input.classList.add("is-valid")
					valid[1]=true
				}
				else{
					text.innerHTML="invalid email address"
					input.classList.remove("is-valid")
					input.classList.add("is-invalid")
					valid[1]=false
				}
			}
			if(type == 'phone'){
				if(phonePattern.test(value)){
					text.innerHTML=""
					console.log("wow")
					input.classList.remove("is-invalid")
					input.classList.add("is-valid")
					valid[2]=true
				}
				else{
					text.innerHTML="invalid phone, should be 11 digits"
					input.classList.remove("is-valid")
					input.classList.add("is-invalid")
					valid[2]=true
				}
			}	
			if(type == "address"){
				if(value==""){
					text.innerHTML="invalid address, should not be empty"
					input.classList.remove("is-valid")
					input.classList.add("is-invalid")
					valid[3]=false
				}
				else{
					text.innerHTML=""
					input.classList.remove("is-invalid")
					input.classList.add("is-valid")
					valid[3]=true
				}
			}
			if(type == "date"){
				if(value==""){
					text.innerHTML="select a date"
					input.classList.remove("is-valid")
					input.classList.add("is-invalid")
					valid[4]=false
				}
				else{
					text.innerHTML=""
					input.classList.remove("is-invalid")
					input.classList.add("is-valid")
					valid[4]=true
				}
			}		
		}

		function checkForm(){
			checkInput('name')
			checkInput('email')
			checkInput('phone')
			checkInput('address')
			checkInput('date')
			if(valid[0] && valid[1] && valid[2] && valid[3] && valid[4] ){
				location.assign('thank.html')
			}
		}