// function test() {
//   for (var i = 0; i < 10; i++) {
//     for (var j = 0; j < 10; j++) {
//       if (i + j == 15) {
//         //code to Break out of both loops here
//           console.log("J: ", j);
//           break;
//       }
//       }

//       console.log("i: ",i);
//   }

//   //Resume from here
//   var a = 5 + 6;
//   console.log(a);
// }

// // console.log(101 ** 0.5);

// // test();

// // let d=√((x_2-x_1)²+(y_2-y_1)²)

// var people = [
//   {
//     name: "Rahul",
//     dob: "12-06-2000",
//     location: { x: 1, y: 10 },
//   },
//   {
//     name: "Priti",
//     dob: "02-02-2010",
//     location: { x: 10, y: 15 },
//   },
//   {
//     name: "Ashish",
//     dob: "15-05-19840",
//     location: { x: 5, y: 6 },
//   },
// ];

// let calculateDistance = (x, y) => {
//     return ((x**2)+(y**2))** 0.5
// }

// function addDistance(people) {
//   //  code to add an distance attribute to each
//   //  person object from {x: 0, y: 0}
//     people.forEach(p => {
//         let distance = calculateDistance(p.location.x, p.location.y);
//         p.distance = distance;
//     });
    
// }

// addDistance(people);

// console.log(people);

// // Expected Output:
// var people = [
//   {
//     name: "Rahul",
//     dob: "12-06-2000",
//     location: { x: 1, y: 10 },
//     distance: 10.05,
//   },
//   {
//     name: "Priti",
//     dob: "02-02-2010",
//     location: { x: 10, y: 15 },
//     distance: 18.02,
//   },
//   {
//     name: "Ashish",
//     dob: "15-05-19840",
//     location: { x: 5, y: 6 },
//     distance: 7.81,
//   },
// ];

