/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pinenumber;

import java.util.Scanner;

/**
 *
 * @author Master Irfak
 */
public class PineNumber {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Number Input : ");
        int number = input.nextInt();
        for (int i = 1; i <= number; i++) {
            for (int j = 1; j <= number; j++) {
                for (int k = number; k > j; k--) {
                    System.out.print(" ");
                }
                for (int z = 1; z <= (2 * j - 1); z++) {
                    System.out.print("*");
                }
                System.out.println();
            }
        }
    }
}
