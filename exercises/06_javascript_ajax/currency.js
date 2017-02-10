//3ICE: Don't forget to wait for document to fully load! (Took me half an hour to figure out)
$(document).ready(function() {
	$("#search").on('click',
	function(e){
		e.preventDefault();
		var t=$("#currencies")[0]
		jQuery.getJSON("http://api.fixer.io/"+$("#date").val()+"?callback=?", function(data) {
			t.innerHTML="";
			for(key in data.rates){ //var i=0; i<data.rates.length;i++
				var tr = document.createElement("tr");
				var td1 = document.createElement("td");
				var td2 = document.createElement("td");
				td1.appendChild(document.createTextNode(key))
				td2.appendChild(document.createTextNode(data.rates[key]))
				tr.appendChild(td1);
				tr.appendChild(td2);
				t.appendChild(tr);
			}
		});
	})
});
/*
for (var i = 0; i < obj.length; i++) {
    var tr = "<tr>";

    //Verification to add the last decimal 0 
    if (obj[i].value.toString().substring(obj[i].value.toString().indexOf('.'), obj[i].value.toString().length) < 2) 
        obj[i].value += "0";

    // Must not forget the $ sign 
    tr += "<td>" + obj[i].key + "</td>" + "<td>$" + obj[i].value.toString() + "</td></tr>";

    // We add the table row to the table body
    tbody.innerHTML += tr;
}*/