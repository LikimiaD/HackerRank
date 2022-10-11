using System;
using System.Collections.Generic;
using System.Collections;

namespace ConsoleApp30
{
    class Person
    {
        string name;
        int age;

        public Person(string name, int age)
        {
            this.name = name;
            this.age = age;
        }

        public string Name { get => name; set => name = value; }
        public int Age { get => age; set => age = value; }

        public override string ToString()
        {
            return name + "  " + age;
        }
        public static bool operator ==(Person d1, Person d2)
        {
            bool r = false;
            if (d1.name == d2.name && d1.age == d2.age) r = true;
            return r;
        }
        public static bool operator !=(Person d1, Person d2)
        {

            return d1.name != d2.name || d1.age != d2.age;
        }

    }
    class MyInt : IComparer
    {
        Person[] m;
        int count;
        public MyInt(int capacity)
        {
            this.m = new Person[capacity];
            count = 0;
        }
        public void Add(Person item)
        {
            if (count == m.Length)
            {
                Person[] temp = new Person[m.Length + 1];
                Array.Copy(m, temp, m.Length);
                m = temp;
            }
            m[count] = item;
            count++;
        }
        public int Capacity
        {
            get { return m.Length; }
        }
        public int Count
        {
            get { return count; }
        }
        public Person this[int index]
        {
            get { return m[index]; }
        }
        public System.Collections.IEnumerator GetEnumerator()
        {
            for (int i = 0; i < count; i++)
            {
                yield return m[i];
            }
        }
        public bool Contains(Person item)
        {
            for (int i = 0; i < count; i++)
            {
                if (m[i] == item) return true;
            }
            return false;
        }
        public void Sort()
        {
            Array.Sort(m, 0, count, this);
        }

        public int Compare(object x, object y)
        {
            Person p1 = (Person)x;
            Person p2 = (Person)y;

            return p1.Age.CompareTo(p2.Age);
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            /*
             * Функция Add имеется ( стоковая )
             */
            MyInt ob = new MyInt(10); // [int 10]
            ob.Add(new Person("t", 18)); //
            Console.WriteLine("Подсчет количества персон");
            Console.WriteLine(ob.Count);
            Console.WriteLine("Подсчет количества слотов");
            Console.WriteLine(ob.Capacity);
            ob.Add(new Person("tt", 17)); 
            ob.Add(new Person("ttt", 21));
            Console.WriteLine("Подсчет количества персон (добавили 2)");
            Console.WriteLine(ob.Count);
            Console.WriteLine("Подсчет количества слотов");
            Console.WriteLine(ob.Capacity);
            Console.WriteLine("Перебор всех персон (Способ for)");
            for (int i = 0; i < ob.Count; i++)
            {
                Console.WriteLine(ob[i]);
            }
            Console.WriteLine("Перебор всех персон (Способ foreach)");
            foreach (Person item in ob)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine(ob.Contains(new Person("t", 28)));
            ob.Sort();
            Console.WriteLine("Ошибка при сортировке?!?");
            Console.WriteLine("Перебор всех персон (Способ foreach) (Попытались в t заменить значение 18 на 28)");
            foreach (Person item in ob)
            {
                Console.WriteLine(item);
            }
        }
    }
}
