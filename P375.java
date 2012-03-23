/**
 * Copyright Tora Holdings Limited 2007 - 2008. All rights reserved. 
 * This software is the confidential and proprietary information of Tora Holdings Limited. 
 * Your rights, if any, with respect to the software are governed by your license agreement with Tora.  
 */

import java.util.Map;
import java.util.SortedMap;
import java.util.TreeMap;

/**
 * @author Peter Levi
 */
//TODO Needs more optimizations, numbers start over at index 6308949
public class P375 {

	public static void main(String[] args) {
		long s = 290797;
		SortedMap<Long, Integer> mins = new TreeMap<Long, Integer>();
		long sum = 0;
		for (int i = 1; i < 2000000001; i++) {
			if (i % 10000000 == 0) {
				System.out.println("i = " + i);
			}
			s = s * s % 50515093;
			mins = addMin(mins, s, i);
			sum += getSum(mins); 
		}
		System.out.println(sum);
	}

	private static long getSum(SortedMap<Long, Integer> mins) {
		int lastIndex = 0;
		long sum = 0;
		for (Map.Entry<Long, Integer> entry : mins.entrySet()) {
			sum += entry.getKey() * (entry.getValue() - lastIndex);
			lastIndex = entry.getValue();
		}
		return sum;
	}

	private static SortedMap<Long, Integer> addMin(SortedMap<Long, Integer> mins, long s, int i) {
		mins = new TreeMap<Long, Integer>(mins.headMap(s));
		mins.put(s, i);
		return mins;
	}
}
