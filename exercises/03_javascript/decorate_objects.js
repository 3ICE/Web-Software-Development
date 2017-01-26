function addPersonMethods(p){
	return {
		"name": p.name,
		"age": p.age,
		greet: function greet(s){
			console.log(s+", my name is "+p.name)
		},
		compareAge: function compareAge(o){
			if(o.age<p.age){
				console.log("My name is "+p.name+" and I'm older than "+o.name)
			}else if(o.age>p.age){
				console.log("My name is "+p.name+" and I'm younger than "+o.name)
			}else{
				console.log("My name is "+p.name+" and I'm equally young as "+o.name)
			}
		},
		namesake: function namesake(o){
			if(p.name==o.name){
				console.log("We have the same name, "+o.name+" and I!")
			}else{
				console.log("We have different names, "+o.name+" and I.")
			}
		}
	}
}