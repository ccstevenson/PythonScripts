from table import Table

if __name__ == '__main__':
    parts = Table.read('parts.txt')
    print parts
    suppliers = Table.read('suppliers.txt')
    print suppliers
    spj = Table.read('spj.txt')
    print spj
    projects = Table.read('projects.txt')
    print projects
    print Table.join(parts,spj)
    print Table.join(suppliers,spj)
    print Table.join(projects,spj)

    print parts.fields
    print parts.select('pno','p2')
    print parts.project('pname','color')
    print parts.project('color')

    suppliers.write('supp2.txt')
    del suppliers
    suppliers = Table.read('supp2.txt')
    print suppliers

    projects.store()
    del projects
    projects = Table.restore('projects.db')
    print projects

    projects.remove('city','Athens')
    projects.insert('j11','Disk','Baltimore')
    print projects

    # Test multi-field join
    foo = Table.read('foo.txt')
    print foo
    bar = Table.read('bar.txt')
    print bar
    print Table.join(foo,bar)

    emp = Table.read('emp.txt')
    print emp
    mgr = Table.read('mgr.txt')
    print mgr
    print Table.join(mgr,emp)
    print Table.join(emp,mgr)