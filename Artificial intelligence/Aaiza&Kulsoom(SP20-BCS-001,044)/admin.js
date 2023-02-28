function quantityUpdate(){
    var category= document.getElementById("category")
    var quantity1= document.getElementById('quantity1')
    var quantity2= document.getElementById('quantity2')
    var categorySel=category.options[category.selectedIndex].text

    if (categorySel==="Cake"){
        quantity1.value="One Pound"
        quantity2.value="Two Pound"
    }
    if (categorySel==="Brownies"){
        quantity1.value="1/2 dozen"
        quantity2.value="1 dozen"
    }
    if (categorySel==="Cookies"){
        quantity1.value="6 pieces"
        quantity2.value="12 pieces"
    }
}

var valid = [true,true]

		function validateInput(type){
			var namePattern = /^[a-zA-Z0-9]([._-](?![._-])|[a-zA-Z0-9]){3,18}[a-zA-Z0-9]$/
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
					valid[0]=false
				}
				else{
					text.innerHTML=""
					input.classList.remove("is-invalid")
					input.classList.add("is-valid")
					valid[0]=true
				}
			}
			if(type == 'pwd'){
				if(passwordPattern.test(value)){
					text.innerHTML=""
					input.classList.remove("is-invalid")
					input.classList.add("is-valid")
					valid[1]=true
				}
				else{
					text.innerHTML="Length should be 8 or more characters, contain a number, upper and lowercase, and *&$!"
					input.classList.remove("is-valid")
					input.classList.add("is-invalid")
					valid[1]=false
				}
			}
			
		}

		function validateSignIn(){
			validateInput('username')
			validateInput('pwd')
			if(valid[0] && valid[1]){
                location.assign('adminViewProduct.html');
			}
		}