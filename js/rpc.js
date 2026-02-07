function demo(){
    let input = "";


    process.stdin.on("data", chunk => {
    input += chunk; 
    });

    process.stdin.on("end",()=>{
        
        const parsedData = JSON.parse(input);
        parsedData["params"]={
            "1":"this is new object"
        }
        process.stdout.write(JSON.stringify(parsedData));
    })
    
    return "this is the demo text to be returned"
}
demo()
