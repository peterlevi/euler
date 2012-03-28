import java.util.Calendar;

/**
 * @author Peter Levi
 */
public class P019 {
    public static void main(String[] args) {
        Calendar cal = Calendar.getInstance();
        cal.set(1901, Calendar.JANUARY, 1);
        int cnt = 0;
        while (cal.get(Calendar.YEAR) < 2001) {
            if (cal.get(Calendar.DAY_OF_WEEK) == Calendar.SUNDAY) {
                cnt++;
//                System.out.println(cal.getTime().toString());
            }
            cal.add(Calendar.MONTH, 1);
        }
        System.out.println(cnt);
    }
}
