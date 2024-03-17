import 'package:flutter/material.dart';

class MenuBottom extends StatefulWidget {
  const MenuBottom({
    Key? key,
  }) : super(key: key);

  @override
  _MenuBottomState createState() => _MenuBottomState();
}

class _MenuBottomState extends State<MenuBottom> {
  int _selectedIndex = 0;

  @override
  Widget build(BuildContext context) {
    return BottomNavigationBar(
      onTap: (int index) {
        switch (index) {
          case 0:
            Navigator.pushNamed(context, '/');
            break;
          case 1:
            Navigator.pushNamed(context, '/test');
            break;
          default:
        }
        setState(() {
          _selectedIndex = index;
        });
      },
      currentIndex: _selectedIndex,
      selectedItemColor: Colors.red,
      unselectedItemColor: Colors.grey,
      items: [
        const BottomNavigationBarItem(icon: Icon(Icons.calculate), label: 'Product'),
        BottomNavigationBarItem(
          icon: Image.asset("assets/images/clothes.png", width: 24, height: 24),
          label: 'Clothes',
        ),
      ],
    );
  }
}

