/*
 * Basic no frills app which integrates the ZBar barcode scanner with
 * the camera.
 * 
 * Created by lisah0 on 2012-02-24
 */
package edu.mit.qr.CameraTest;

import javax.net.ssl.HostnameVerifier;
import javax.net.ssl.HttpsURLConnection;
import javax.net.ssl.SSLSession;

import net.sourceforge.zbar.Config;
import net.sourceforge.zbar.Image;
import net.sourceforge.zbar.ImageScanner;
import net.sourceforge.zbar.Symbol;
import net.sourceforge.zbar.SymbolSet;
import android.app.Activity;
import android.content.Intent;
import android.content.pm.ActivityInfo;
import android.hardware.Camera;
import android.hardware.Camera.AutoFocusCallback;
import android.hardware.Camera.PreviewCallback;
import android.hardware.Camera.Size;
import android.net.Uri;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.FrameLayout;
import android.widget.TextView;

public class CameraTestActivity extends Activity
{
    private Camera mCamera;
    private CameraPreview mPreview;
    private Handler autoFocusHandler;
//    private final String DOMAIN = "www.mit.edu";
    private final String DOMAIN = "jennya.scripts.mit.edu/6.857/quartirs_app/";

    TextView scanText;
    Button scanButton;

    ImageScanner scanner;

    private boolean barcodeScanned = false;
    private boolean previewing = true;

    static {
        System.loadLibrary("iconv");
    } 

    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.main);

        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);

        autoFocusHandler = new Handler();
        mCamera = getCameraInstance();

        /* Instance barcode scanner */
        scanner = new ImageScanner();
        scanner.setConfig(0, Config.X_DENSITY, 3);
        scanner.setConfig(0, Config.Y_DENSITY, 3);

        mPreview = new CameraPreview(this, mCamera, previewCb, autoFocusCB);
        FrameLayout preview = (FrameLayout)findViewById(R.id.cameraPreview);
        preview.addView(mPreview);

        scanText = (TextView)findViewById(R.id.scanText);

        scanButton = (Button)findViewById(R.id.ScanButton);

        scanButton.setOnClickListener(new OnClickListener() {
                public void onClick(View v) {
                    if (barcodeScanned) {
                        barcodeScanned = false;
                        scanText.setText("Scanning...");
                        mCamera.setPreviewCallback(previewCb);
                        mCamera.startPreview();
                        previewing = true;
                        mCamera.autoFocus(autoFocusCB);
                    }
                }
            });
    }

    public void onPause() {
        super.onPause();
        releaseCamera();
    }

    /** A safe way to get an instance of the Camera object. */
    public static Camera getCameraInstance(){
        Camera c = null;
        try {
            c = Camera.open();
        } catch (Exception e){
        }
        return c;
    }

    private void releaseCamera() {
        if (mCamera != null) {
            previewing = false;
            mCamera.setPreviewCallback(null);
            mCamera.release();
            mCamera = null;
        }
    }

    private Runnable doAutoFocus = new Runnable() {
            public void run() {
                if (previewing)
                    mCamera.autoFocus(autoFocusCB);
            }
        };

    PreviewCallback previewCb = new PreviewCallback() {
            public void onPreviewFrame(byte[] data, Camera camera) {
                Camera.Parameters parameters = camera.getParameters();
                Size size = parameters.getPreviewSize();

                Image barcode = new Image(size.width, size.height, "Y800");
                barcode.setData(data);

                int result = scanner.scanImage(barcode);
                
                if (result != 0) {
                    previewing = false;
                    mCamera.setPreviewCallback(null);
                    mCamera.stopPreview();
                    SymbolSet syms = scanner.getResults();
                    for (Symbol sym : syms) {
                    	String url = sym.getData();
                    	Log.d("QR CODE SCANNER", "URL: " + url);
                    	establishConnection(url);
                    	barcodeScanned = true;
                    }
                }
            }
        };

    // Mimic continuous auto-focusing
    AutoFocusCallback autoFocusCB = new AutoFocusCallback() {
            public void onAutoFocus(boolean success, Camera camera) {
                autoFocusHandler.postDelayed(doAutoFocus, 1000);
            }
        };
        
    private void openLink(String s) {
    	Intent browserIntent = new Intent(Intent.ACTION_VIEW, Uri.parse(s));
    	startActivity(browserIntent);
    }
        
    private void establishConnection(String s) {
    	HostnameVerifier hostnameVerifier = new HostnameVerifier() {
    	    @Override
    	    public boolean verify(String hostname, SSLSession session) {
    	        HostnameVerifier hv =
    	            HttpsURLConnection.getDefaultHostnameVerifier();
    	        return hv.verify(DOMAIN, session);
    	    }
    	};
    	
    	if (s.matches("(http://|https://)" + DOMAIN + ".*")) {
    		scanText.setText("got MIT!");
    		openLink(s);
    		return;
    	} 
    	else {
    		scanText.setText("barcode result " + s);
    		openLink(s);
    		return;
    	}
    	/*
    	try {
    		CertificateFactory cf = CertificateFactory.getInstance("X.509");
    		InputStream caInput = new BufferedInputStream(new FileInputStream( 
    				"/storage/sdcard0/6.857/" + "Marcelo R Polanco MIT.cer"));
    		Certificate ca;
    		try {
    		    ca = cf.generateCertificate(caInput);
    		    System.out.println("ca=" + ((X509Certificate) ca).getSubjectDN());
    		} finally {
    		    caInput.close();
    		}

    		// Create a KeyStore containing our trusted CAs
    		String keyStoreType = KeyStore.getDefaultType();
    		KeyStore keyStore = KeyStore.getInstance(keyStoreType);
    		keyStore.load(null, null);
    		keyStore.setCertificateEntry("ca", ca);

    		// Create a TrustManager that trusts the CAs in our KeyStore
    		String tmfAlgorithm = TrustManagerFactory.getDefaultAlgorithm();
    		TrustManagerFactory tmf = TrustManagerFactory.getInstance(tmfAlgorithm);
    		tmf.init(keyStore);

    		// Create an SSLContext that uses our TrustManager
    		SSLContext context = SSLContext.getInstance("TLS");
    		context.init(null, tmf.getTrustManagers(), null);
    		
    		URL url = new URL(s);
        	HttpsURLConnection urlConnection =
        	    (HttpsURLConnection)url.openConnection();
        	urlConnection.setHostnameVerifier(hostnameVerifier);
        	InputStream in = urlConnection.getInputStream();
        	Scanner scan = new Scanner(in).useDelimiter(" ");
        	while (scan.hasNext()) {
        		System.out.println(scan.next());
        	}
    	} catch (IOException e) {
    		e.printStackTrace();
    	} catch (KeyStoreException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (NoSuchAlgorithmException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (CertificateException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (KeyManagementException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    	*/
    }
}
