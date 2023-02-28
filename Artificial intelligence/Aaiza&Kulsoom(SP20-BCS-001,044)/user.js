var valid = [true,true,true,true,true]

		function checkInput(type){
			var namePattern = /^[^1-9]*$/
      var usernamePattern = /^[A-Za-z_0-9]+$/
			var passwordPattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[*&$!]).{8,}$/
      var cnfrmpsdPattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[*&$!]).{8,}$/
			var emailPattern = /^([a-z0-9\.-]+)@([a-z0-9-]+)\.([a-z]{2,8})$/
			var input = document.getElementById(type)
			var text = document.getElementById(type+'Error')
			var form = document.getElementById(type+'Form')
			var value = input.value

			if(type == 'name'){
				console.log(!(namePattern.test(value)))
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
      if(type == 'username'){
				console.log(!(usernamePattern.test(value)))
				if(value=="" || !(usernamePattern.test(value))){
					text.innerHTML="username should only contain letters, numbers and _"
					input.classList.remove("is-valid")
					input.classList.add("is-invalid")
					valid[1]=false
				}
				else{
					text.innerHTML=""
					input.classList.remove("is-invalid")
					input.classList.add("is-valid")
					valid[1]=true
				}
			}
			if(type == 'email'){
				if(emailPattern.test(value)){
					text.innerHTML=""
					input.classList.remove("is-invalid")
					input.classList.add("is-valid")
					valid[2]=true
				}
				else{
					text.innerHTML="invalid email address"
					input.classList.remove("is-valid")
					input.classList.add("is-invalid")
					valid[2]=false
				}
			}
      if(type == 'pwd'){
				if(passwordPattern.test(value)){
					text.innerHTML=""
					input.classList.remove("is-invalid")
					input.classList.add("is-valid")
					valid[3]=true
				}
				else{
					text.innerHTML="Length should be 8 or more characters, contain a number, upper and lowercase, and *&$!"
					input.classList.remove("is-valid")
					input.classList.add("is-invalid")
					valid[3]=false
				}
			}
      if(type == 'pwd1'){
				if(cnfrmpsdPattern.test(value)){
          var pass = document.getElementById('pwd').value
          if(pass === value){
            text.innerHTML=""
					  input.classList.remove("is-invalid")
					  input.classList.add("is-valid")
					  valid[4]=true
          }
          else{
            text.innerHTML="Passwords don't match"
					  input.classList.remove("is-valid")
					  input.classList.add("is-invalid")
					  valid[4]=false
          }
					
				}
				else{
					text.innerHTML="Length should be 8 or more characters, contain a number, upper and lowercase, and *&$!"
					input.classList.remove("is-valid")
					input.classList.add("is-invalid")
					valid[4]=false
				}
			}
		}

		function checkForm(){
			checkInput('name')
			checkInput('username')
			checkInput('email')
			checkInput('pwd')
			checkInput('pwd1')
			if(valid[0] && valid[1] && valid[2] && valid[3] && valid[4]){
				
				return true;
			}
			else{
				return false;
			}
		}

        var valid1 = [true,true]

		function checkInput1(type){
			var namePattern = /^[A-Za-z_0-9]+$/
			var passwordPattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[*&$!]).{8,}$/
			var input = document.getElementById(type)
			var text = document.getElementById(type+'Error')
			var form = document.getElementById(type+'Form')
			var value = input.value

			if(type == 'username'){
				console.log(!(namePattern.test(value)))
				if(value=="" || !(namePattern.test(value))){
					text.innerHTML="username should only contain letters, numbers and _"
					input.classList.remove("is-valid")
					input.classList.add("is-invalid")
					valid1[0]=false
				}
				else{
					text.innerHTML=""
					input.classList.remove("is-invalid")
					input.classList.add("is-valid")
					valid1[0]=true
				}
			}
			if(type == 'pwd'){
				if(passwordPattern.test(value)){
					text.innerHTML=""
					input.classList.remove("is-invalid")
					input.classList.add("is-valid")
					valid1[1]=true
				}
				else{
					text.innerHTML="Length should be 8 or more characters, contain a number, upper and lowercase, and *&$!"
					input.classList.remove("is-valid")
					input.classList.add("is-invalid")
					valid1[1]=false
				}
			}
			
		}

		function checkForm1(){
			checkInput('username')
			checkInput('pwd')
			if(valid1[0] && valid1[1]){
				return true;
			}
			else{
				return false;
			}
		}