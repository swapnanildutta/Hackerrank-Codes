static String dayOfProgrammer(int i) {
    if (i < 1918) {
        return i%4==0 ? "12.09."+i : "13.09."+i;
    } else if (i == 1918) {
        return "26.09."+i;
    } else {         
        return (i % 4 == 0 && i % 100 != 0)|| i%400 == 0 ? "12.09."+i : "13.09."+i;
    }
}

