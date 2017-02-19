package studentCode;

import java.util.ArrayList;

public class MyPersonListV1 {
	//DO NOT CHANGE THIS LINE
	ArrayList<Person> people;

	
	
	/**
	 * Instantiates the "people" variable as a new ArrayList of
	 * references to Person objects.
	 */
	public MyPersonListV1(){
		people = new ArrayList<Person>();
	}
	
	/**
	 * A copy constructor which makes the right kind of copy considering
	 * a Person is mutable.
	 */
	public MyPersonListV1(MyPersonListV1 other) { 
		people = new ArrayList<Person>(other.people.size());
		for (Person p : other.people) {
			this.people.add(new Person (p));
			}
	}
	
	/** Adds the parameter to the end of the list.  With ArrayList this
	 *  will be much shorter in terms of code than you will see in the
	 *  V2 approach using arrays.  Of course here, we have no control 
	 *  over how much "spare" space is allocated in the interest of
	 *  time efficiency behind the scenes.
	 *  
	 *  Note that you want to make sure that you don't just do a reference
	 *  copy of the newMember Person since it is mutable.
	 */
	public void addItem(Person newMember){	
		people.add(new Person(newMember));
	}
	
	/** Gives each person in the list a raise of $1000.  Note that the objects
	 *  are mutable, which means you can use a for-each style loop as you update.
	 */
	public void giveRaises(){
		for ( Person p: people) {
			p.acceptRaise(1000);
		}
	}
	
	/** Returns the sum of the salaries of all people in the list.
	 */
	public int getTotalOfSalaries(){
		int totalSalary = 0;
		for ( Person p: people) {
			totalSalary = totalSalary + p.getSalary();
		}
		return totalSalary;
	}

	/** Returns the number of people in the list with a name
	 *  that matches the parameter (possibly 0).
	 */
	/**
	 * @param searchName
	 * @return
	 */
	public int count(String searchName){
		int totalName = 0;
		for ( Person p: people) {
			if (p.getName().compareTo(searchName) == 0){
				totalName++;
			}
		}
		return totalName;
	}
	
	/** Removes ALL people from the list whose names match the parameter
	 *  (possibly more than one person).  Consider that a for-each style
	 *  loop cannot be used unless you create a shadow.  There are code
	 *  examples in the posted slides that will be useful here.
	 */
	public void remove(String name){
		for ( Person p: people) {
			if (p.getName().compareTo(name) == 0){
				people.remove(p);
			}
		}
	}
}




