function appendCharacters(s: string, t: string): number {
    let s_left=0,t_left=0;

    while(s_left<s.length && t_left<s.length){
        if (s[s_left]==t[t_left]){
            t_left++
        }
        s_left++
    }
    return t.length-t_left
    
};