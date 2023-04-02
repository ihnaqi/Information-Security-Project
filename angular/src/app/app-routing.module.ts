import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AppointmentsListComponent } from './components/appointments-list/appointments-list.component';
import { AppointmentsDetailsComponent } from './components/appointments-details/appointments-details.component';
import { AddAppointmentsComponent } from './components/add-appointments/add-appointments.component';
//

import { PrescriptionsListComponent } from './components/prescriptions-list/prescriptions-list.component';
// import { PrescriptionsDetailsComponent } from './components/prescriptions-details/prescriptions-details.component';
// import { AddPrescriptionsComponent } from './components/add-prescriptions/add-prescriptions.component';


import { DoctorsListComponent } from './components/doctors-list/doctors-list.component';
import { DoctorsDetailsComponent } from './components/doctors-details/doctors-details.component';

//AUTH
import { UserLoginComponent } from "./components/user-login/user-login.component";
import { UserProfileComponent } from './components/user-profile/user-profile.component';
import { AuthGuard } from "./components/user-login/auth.guard";

const routes: Routes = [
  // { path: '', redirectTo: 'Clients', pathMatch: 'full' },
  { path: '', component: UserProfileComponent, pathMatch: 'full', canActivate: [AuthGuard] },

  { path: 'Appointments', component: AppointmentsListComponent,canActivate: [AuthGuard] },
  { path: 'Appointments/:id', component: AppointmentsDetailsComponent, canActivate: [AuthGuard] },
  { path: 'Add-Appointment', component: AddAppointmentsComponent, canActivate: [AuthGuard] },
///

{ path: 'Prescriptions', component: PrescriptionsListComponent,canActivate: [AuthGuard] },
// { path: 'Prescriptions/:id', component: PrescriptionsDetailsComponent, canActivate: [AuthGuard] },
{ path: 'Prescriptions/:id', component: PrescriptionsListComponent },
// { path: 'Add-Prescription', component: AddPrescriptionsComponent, canActivate: [AuthGuard] },
// //

  //Doctors
  { path: 'Doctors', component: DoctorsListComponent, canActivate: [AuthGuard] },
  { path: 'Doctors/:id', component: DoctorsDetailsComponent,  },

  //Login
  { path: 'login', component: UserLoginComponent },
  { path: 'user-profile/:id', component: UserProfileComponent, canActivate: [AuthGuard] },

  //Other Redirect
  { path: '**', redirectTo: '' }

];
export const routing = RouterModule.forRoot(routes);

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
