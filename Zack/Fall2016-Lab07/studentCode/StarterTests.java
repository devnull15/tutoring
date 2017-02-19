package studentCode;

import static org.junit.Assert.*;

import org.junit.Test;

import studentCode.MyPersonListV2;
import studentCode.Person;



public class StarterTests  {

	@Test
	public void testConstructor() {
		MyPersonListV1 localList1 = new MyPersonListV1();
		assertTrue(localList1 != null);
		assertTrue(localList1.people != null);
		assertTrue(localList1.people.size() == 0);
		
		MyPersonListV2 localList2 = new MyPersonListV2();
		assertTrue(localList2 != null);
		assertTrue(localList2.people != null);
		assertTrue(localList2.people.length == 0);
	}

	@Test
	public void testAdd() {
		Person p1 = new Person("Sam");
		Person p2 = new Person("Pat");
		Person p3 = new Person("Sasha");
		
		MyPersonListV1 localPersonList1 = new MyPersonListV1();
		localPersonList1.addItem(p1);
		localPersonList1.addItem(p2);
		localPersonList1.addItem(p3);
		
		assertEquals(p1, localPersonList1.people.get(0));
		assertEquals(p2, localPersonList1.people.get(1));
		assertEquals(p3, localPersonList1.people.get(2));
		

		
		MyPersonListV2 localPersonList2 = new MyPersonListV2();
		localPersonList2.addItem(p1);
		localPersonList2.addItem(p2);
		localPersonList2.addItem(p3);
		
		assertEquals(p1, localPersonList2.people[0]);
		assertEquals(p2, localPersonList2.people[1]);
		assertEquals(p3, localPersonList2.people[2]);

	}



}

