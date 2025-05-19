import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('GrievanceAI'),
      ),
      body: Center(
        child: ElevatedButton(
          onPressed: () {
            // Navigate to complaint submission screen
          },
          child: const Text('Submit Complaint'),
        ),
      ),
    );
  }
}
