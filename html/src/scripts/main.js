import Vue from 'vue';

window.onload = function () {
	new Vue({
		'el': 'app', 
		'data': {
			'title': "Elastic Food"
		},	
		'template': '<h1>{{ title }}</h1>'
	});
};