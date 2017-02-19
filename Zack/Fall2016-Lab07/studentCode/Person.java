package studentCode;



/** Here we provide a concrete implementation of a Person for use with the lab.
 */

public class Person {
	private String name;
	private int salary;
	
	public Person(String nameIn) {
		name = nameIn;
		salary = 10000;
	}
	
	public Person(Person other) {
		this.name = other.name;
		this.salary = other.salary;
	}
	public String getName() {
		return name;
	}
	
	public int getSalary() {
		return salary;
	}
	
	public void acceptRaise(int amount) {
		salary += amount;
	}
	
	@Override
	public boolean equals(Object other) {
		if (other==null) {
			return false;
		}
		try {
			Person local = (Person)other;
			return this.name.equals(local.name);
		}
		catch (Exception e) {
			return false;
		}
	}
	
}