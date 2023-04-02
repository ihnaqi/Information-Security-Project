import { Component, OnInit } from '@angular/core';
import { Appointment } from 'src/app/models/appointment.model';
import { AppointmentService } from 'src/app/services/appointment.service';

import { ActivatedRoute } from "@angular/router";

import { Doctor} from 'src/app/models/doctor.model';
import { DoctorService } from 'src/app/services/doctor.service';

import { Router } from '@angular/router';

@Component({
  selector: 'app-add-appointment',
  templateUrl: './add-appointments.component.html',
  styleUrls: ['./add-appointments.component.css']
})

export class AddAppointmentsComponent implements OnInit {
  appointment: Appointment = {
    patient:'',
    doctor:'',
    description:''
  };
  submitted = false;
  doctors?: Doctor[];

  constructor (private appointmentService: AppointmentService,
    private clientService: DoctorService,
    private router: Router,
    private activatedRoute: ActivatedRoute){

      
     }

  ngOnInit(): void {
    this.retrieveAppointments();
  }

  retrieveAppointments(): void {
    this.clientService.getAll()
      .subscribe(
        data => {
          this.doctors = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  saveAppointment(): void {
    
    // const userData = ;
 
    const userData = JSON.parse(localStorage.getItem('userData')|| '{}')
 
    const data = {
      
      description: this.appointment.description,
      doctor:this.appointment.doctor,
      patient: ""+userData.user_id
      // patient: 3
    };
    
    this.appointmentService.create(data)
      .subscribe(
        response => {
          console.log(response);
          this.router.navigate(['/View-Doctors/'+this.appointment.patient]);
        },
        error => {
          console.log(error);
        });
  }

  newAppointment(): void {
    this.submitted = false;
    this.appointment = {
      
    };
     
  }
}