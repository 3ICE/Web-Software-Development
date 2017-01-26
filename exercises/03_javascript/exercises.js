function keywordusage(str,arr){
	ret = [];
	//console.log(arr.length)
	for(var i=0;i<arr.length;i++){
	var pos = str.search(arr[i]);
	//console.log(i)
	if(pos>0){
		ret[i]=true;
	}
	else{
		ret[i]=false;
	}
 }
	return ret
}

function frequencies(text,wordlist){
	var ret = {};
	var r;
	for(var j = 0; j < wordlist.length; j++){
		r=new RegExp(wordlist[j], 'g')
		if(text.match(r)){
			//console.log(text.match(r));
			ret[wordlist[j]] = text.match(r).length;
			//console.log(ret);
		}
	}
	return ret;
}

function rotate(array, steps=1){
	if(steps<0){
		steps = -steps;
		while(steps--){
			array.push(array.shift());
		}
	}else{
		while(steps--){
			array.unshift(array.pop());
		}
	}
	return array;
}

