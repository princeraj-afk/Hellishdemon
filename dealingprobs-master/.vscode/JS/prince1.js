// Dont use var
// let create a local variable inside {} even if does exist
// const arr will let u add but not replace orignal ones
// parsing a variable is necesary
//Using let or const before variable assignment

/* writing types
1. camelCase
2. kebab-case
3. snake_case
4. PascalCase*/

/* 
primitive dats type(stack):
        string,numbers,boolean,null,undefined,symbol

reference data type(heap):
        array,obj literals(dict),functions,Dates
*/

console.time('a')
console.timeEnd('a')

console.log('My name is prince raj')
console.table({prince:34,aryan:46})

const owner = "prince raj"
console.log(owner)
console.log(owner.lastIndexOf('r'))
console.log(owner.includes(" "))
console.log(owner.substring(1,5))

var city = "mdb"
const arr = [2,2,2,2,3,4]
arr.push(9)
arr.unshift(34)
arr.pop()
arr.shift()
arr.splice(2,1)
arr.reverse()
console.log(arr)

let d = String(new Date())
console.log(d)

let p = 34.9438
console.log(p.toFixed(3))

// myHtml = `<h1>Hello ${owner},</h1>
// <h1>buenos dias,</h1>
// <h1>Have a nice day!</h1>`
// document.body.innerHTML = myHtml

// if-->switch
// else-->case

arr.forEach(function(element){console.log(element)})
console.clear()


let a = document.images
console.log(a)
