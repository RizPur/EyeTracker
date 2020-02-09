function change(letter){
    let tex = document.getElementById("main").innerHTML
    console.log(tex);
    let arr = tex.split("");
    console.log(arr);
    if(count === 0){
        arr=[];
        count++;
    }
    switch(letter){
        case 'a':
            console.log('You pressed A');
            arr.push('a');
            console.log(arr);
            break;
        case 'b':
            arr.push('b');
            break;
        case 'c': 
            arr.push('c');
            break;
        case 'd': 
            arr.push('d');
            break;
        case 'e': 
            arr.push('e');
            break;
        case 'f': 
            arr.push('f');
            break;
        case 'g': 
            arr.push('g');
            break; 
        case 'h': 
            arr.push('h');
            break;
        case 'i': 
            arr.push('i');
            break;
        case 'j': 
            arr.push('j');
            break;
        case 'k': 
            arr.push('k');
            break;
        case 'l':
            arr.push('l');
            break;
        case 'm': 
            arr.push('m');
            break;
        case 'n': 
            arr.push('n');
            break; 
        case 'o': 
            arr.push('o');
            break;
        case 'p': 
            arr.push('p');
            break;
        case 'q': 
            arr.push('q');
            break;
        case 'r':
            arr.push('r');
            break;
        case 's': 
            arr.push('s');
            break;
        case 't':
            arr.push('t');
            break;
        case 'u':
            arr.push('u');
            break;
        case 'v':
            arr.push('v');
            break;
        case 'w':
            arr.push('w');
            break;
        case 'x': 
            arr.push('x');
            break;
        case 'y': 
            arr.push('y');
            break;
        case 'z': 
            arr.push('z');
            break;    
        case '<=':
            arr.pop();
            break;
    }
    if(arr.length === 1){
       arr[0] = arr[0].toUpperCase();  
    }
    tex = arr.join("");
    console.log(tex);
    document.getElementById("main").innerHTML = tex;
}
var count = 0;
