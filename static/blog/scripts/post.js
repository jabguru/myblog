var submit = document.getElementById('form-submit');
var commName = document.getElementById('comm-name');
var commEmail = document.getElementById('comm-email');
var commComm = document.getElementById('comm-comm');

function submitForm(){
	if (commName.value.length > 0 && commEmail.value.length > 0 && commComm.value.length > 0){
		alert("Thanks for your comment!");
	}
	else{
		alert('Please fill the fields');
	}
	
}

submit.addEventListener('click', submitForm);