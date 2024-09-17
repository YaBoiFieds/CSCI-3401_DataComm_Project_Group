/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package RandomNumberGenerator;

/**
 *
 * @author natha
 */
public class RandomNumberGenerator {
    
    
    public static void main( String args[] ) {
        
        int min = 1;
        int max = 75;

System.out.println("Random value in int from "+min+" to "+max+ ":");

int random_source = (int)Math.floor(Math.random()*(max-min+1)+min);
int random_destination = (int)Math.floor(Math.random()*(max-min+1)+min);

System.out.println("Source Node"+" " +random_source);
System.out.println("Destination Node"+" " +random_destination);
        
    }
    
}
