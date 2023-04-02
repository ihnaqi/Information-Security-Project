import { Component, OnInit } from '@angular/core';
import { Doctor } from 'src/app/models/doctor.model';
import { DoctorService } from 'src/app/services/doctor.service';


@Component({
  selector: 'app-doctor-list',
  templateUrl: './doctors-list.component.html',
  styleUrls: ['./doctors-list.component.css']
})


export class DoctorsListComponent implements OnInit {

  doctors?: any;
  doctor_name = '';
  currentDoctor: Doctor = {};
  currentIndex = -1;
  title = '';
  page = 1;
  count = 0;
  tableSize = 10;

  constructor(private doctorService: DoctorService) { }

  ngOnInit(): void {
    this.retrieveDoctors();
  }

  
  retrieveDoctors(): void {
    this.doctorService.getAll()
      .subscribe(
        data => {
          this.doctors = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }
  
  refreshList(): void {
    this.retrieveDoctors();
    this.currentDoctor = {};
    this.currentIndex = -1;
  }
    
  tabSize(event:any){
    this.page = event;
    //this.retrieveClients();
  }  

  tableData(event:any): void {
    this.tableSize = event.target.value;
    this.page = 1;
    this.retrieveDoctors();
  } 

  setActiveDoctor(doctor: Doctor, index: number): void {
    this.currentDoctor =doctor;
    this.currentIndex = index;
  }

  searchDoctors(): void {
    this.currentDoctor = {};
    this.currentIndex = -1;

    this.doctorService.findByDoctorName(this.doctor_name)
      .subscribe(
        data => {
          this.doctors = data;
          this.page=1
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

}


