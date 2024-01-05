import java.util.HashMap;

/**
 * is
 */
public class is {  
    public static boolean pre(String A , String B) {  
         HashMap<Character , Integer> map = new HashMap<>();  
        for( int i=0; i<A.length(); i++){ 
            if(map.containsKey(A.charAt(i))){ 
                int v = map.get(A.charAt(i)); 
                map.put(A.charAt(i) , v+1);
            } 
            else { 
                  map.put(A.charAt(i) , 1);
            }
        } 
        for( int i=0; i<B.length(); i++){ 
            if(!map.containsKey(B.charAt(i))){ 
                     return false;
             }
        } 
        return true;

    }

    public static void main(String[] args) {
        String A ="xyz"; 
        String B ="zx"; 
       
        System.out.println(pre(A, B));
    }
}