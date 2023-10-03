function longestCommonPrefix(strs){
    if(strs.length === 0) return ''
    let prefix = strs[0].trim()
    for(let i = 0; i<strs.length; i++){
        while(strs[i].indexOf(prefix) !== 0){
            console.log(strs[i], 'i');
            prefix = prefix.slice(0, prefix.length-1)
            console.log(prefix, 'prefix');
            if(prefix === '') return ''
        }
    }
    console.log(strs[0], 'hello')
    return prefix
  };
  
  const strs= ["flower","flow","flight"]
  const result = longestCommonPrefix(strs)
  console.log(result)

for(let i=0; i<=3; i++){
    for(j=0; j<=3; j++){
        console.log(i, j);
    }
}