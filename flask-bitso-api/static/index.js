document.addEventListener('DOMContentLoaded', () => {
	document.querySelector('#converter').onsubmit = () => {

			const request = new XMLHttpRequest();
			const currency = document.querySelector('#currency').value;

			request.open('POST', '/bitso');

			request.onload = () => {
				const data = JSON.parse(request.responseText);
                 if( data.success ){
				    document.querySelector('#result').innerHTML = `Current price for ${currency} is ${data.payload.last}`;
				 } else {
				    document.querySelector('#result').innerHTML = "Currency doesn't exist!";
				 }
			}

			const data = new FormData();
			data.append('currency', currency);

			request.send(data);

			return false;

	}
});